import json
import os
from datetime import datetime
import pandas as pd

# আমাদের তৈরি করা মডিউলগুলো ইম্পোর্ট করা হচ্ছে
from app.llm.ollama_client import query_ollama
from app.analysis.sentiment import analyze_brand_response
from app.analysis.sov import calculate_sov
from app.core.config import BRAND, COMPETITORS, BUYER_PROMPTS

def run_analysis():
    print("Starting AgenticSOV Analysis Pipeline...")
    print(f"Brand: {BRAND}")
    print(f"Competitors: {COMPETITORS}")
    print(f"Total Buyer Prompts: {len(BUYER_PROMPTS)}")
    print("=========================================\n")

    all_brands = [BRAND] + COMPETITORS
    recommendation_counts = {brand: 0 for brand in all_brands}
    results_details = []

    # প্রতিটি Buyer Prompt-এর জন্য লুপ চালানো হচ্ছে (Phase 14)
    for idx, prompt in enumerate(BUYER_PROMPTS, 1):
        print(f"[{idx}/{len(BUYER_PROMPTS)}] Running query: '{prompt}'")
        
        # Ollama থেকে উত্তর জেনারেট করা হচ্ছে
        answer = query_ollama(prompt)
        
        # প্রতিটি ব্র্যান্ডের রিকমেন্ডেশন ও সেন্টিমেন্ট অ্যানালাইসিস করা হচ্ছে
        brand_analyses = {}
        for brand in all_brands:
            print(f"  Analyzing Brand: {brand}...")
            analysis = analyze_brand_response(brand, answer)
            brand_analyses[brand] = analysis
            
            # যদি ব্র্যান্ডটি explicitly recommended হয়, তবে কাউন্ট বাড়ানো হচ্ছে
            if analysis.get("recommended") is True:
                recommendation_counts[brand] += 1
        
        # ডিটেইলড রেজাল্ট সেভ করা হচ্ছে
        results_details.append({
            "query": prompt,
            "raw_answer": answer,
            "analyses": brand_analyses
        })
        print("-" * 50)

    # Share of Voice (SOV) ক্যালকুলেট করা (Phase 13/14)
    sov = calculate_sov(recommendation_counts)

    # টার্মিনালে আউটপুট প্রিন্ট করা (Phase 15)
    print("\n===== AGENTICSOV RESULT =====")
    print("Recommendation Count:")
    for brand, count in recommendation_counts.items():
        print(f"  {brand}: {count}")

    print("\nShare of Voice:")
    for brand, percentage in sov.items():
        print(f"  {brand}: {percentage}%")
    print("=============================\n")

    # নিশ্চিত করা হচ্ছে যাতে output ফোল্ডারটি কম্পিউটারে তৈরি থাকে
    os.makedirs("data/results", exist_ok=True)


    # ==========================================
    # [Phase 16] - JSON আকারে ফলাফল সেভ করা শুরু
    # ==========================================
    print("Saving JSON Report...")
    output_json = {
        "brand": BRAND,
        "competitors": COMPETITORS,
        "queries": len(BUYER_PROMPTS),
        "recommendation_count": recommendation_counts,
        "share_of_voice": sov,
        "results": results_details,
        "timestamp": datetime.utcnow().isoformat()
    }

    json_path = "data/results/analysis.json"
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(output_json, file, indent=2, ensure_ascii=False)
    print(f"[✓] JSON Report saved successfully at: {json_path}")
    # ==========================================
    # [Phase 16] - শেষ
    # ==========================================


    # ==========================================
    # [Phase 17] - Marketer-friendly CSV তৈরি করা শুরু
    # ==========================================
    print("Saving CSV Report...")
    rows = []
    for brand, count in recommendation_counts.items():
        rows.append({
            "Brand": brand,
            "Recommendations": count,
            "Share of Voice (%)": sov.get(brand, 0.0)
        })
    df = pd.DataFrame(rows)
    csv_path = "data/results/sov_report.csv"
    df.to_csv(csv_path, index=False)
    print(f"[✓] CSV Report saved successfully at: {csv_path}")
    # ==========================================
    # [Phase 17] - শেষ
    # ==========================================


if __name__ == "__main__":
    run_analysis()