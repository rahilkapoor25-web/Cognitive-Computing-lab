import pandas as pd

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)

roll = "1024170352"

fixed_entries = [
    {"question": "what is the annual fee", "answer": "The annual fee is Rs 500.",
     "keywords": "fee cost price charge", "category": "billing"},
    {"question": "how to reset password", "answer": "Go to Settings > Reset Password.",
     "keywords": "password reset login", "category": "account"},
    {"question": "what are your working hours", "answer": "We are open 9 AM to 5 PM.",
     "keywords": "hours timing open time", "category": "general"},
    {"question": "how can i pay the fee", "answer": "You can pay via UPI, card, or net banking.",
     "keywords": "pay payment upi fee", "category": "billing"},
]

# last two digits of the roll number
d1 = int(roll[-2])   # 5
d2 = int(roll[-1])   # 2

categories = ["billing", "account", "general"]

cat1 = categories[d1 % 3]
cat2 = categories[d2 % 3]

print("Roll number:", roll)
print("digit", d1, "-> category[", d1 % 3, "] =", cat1)
print("digit", d2, "-> category[", d2 % 3, "] =", cat2)

# 2 personalized entries built from those digits
my_entries = [
    {"question": "where is your office located",
     "answer": "Our office is at Block C, Ground Floor, near the main gate.",
     "keywords": "office location address", "category": cat1},
    {"question": "do you work on saturdays",
     "answer": "We work on the first and third Saturday, 10 AM to 2 PM.",
     "keywords": "saturday weekend holiday", "category": cat2},
]

df = pd.DataFrame(fixed_entries + my_entries)

print("\nFinal 6-row DataFrame:")
print(df)

#q2
stopwords = ["what", "is", "the", "a", "an", "how", "to", "do", "i", "my",
             "can", "are", "your", "of", "in", "for", "me", "you", "and"]


def score_query(query, df):
    query_words = [w for w in query.lower().split() if w not in stopwords]
    if len(query_words) == 0:
        return pd.DataFrame()

    results = []

    for i in range(len(df)):
        text = df.loc[i, "keywords"] + " " + df.loc[i, "question"]
        text_words = text.lower().split()

        matched = [w for w in query_words if w in text_words]
        score = len(matched)
        confidence = score / len(query_words)

        if score > 0:
            results.append({
                "question": df.loc[i, "question"],
                "answer": df.loc[i, "answer"],
                "category": df.loc[i, "category"],
                "score": score,
                "confidence": round(confidence, 2),
            })

    result_df = pd.DataFrame(results)
    if len(result_df) > 0:
        result_df = result_df.sort_values("confidence", ascending=False).reset_index(drop=True)
    return result_df


print("\nQ2: scoring a query")
print(score_query("how can i reset my password", df))


#q3
def same_category(category_name, df):
    return df[df["category"] == category_name]["question"]


print("\nQ3: questions in category '" + cat1 + "'")
print(same_category(cat1, df))


#q4
print("\nQ4: add a keyword and save to CSV")
print("Chosen entry:", df.loc[0, "question"])
print("Current keywords:", df.loc[0, "keywords"])

new_keyword = input("Enter a new keyword: ")

df.loc[0, "keywords"] = df.loc[0, "keywords"] + " " + new_keyword.lower()
print("Updated keywords:", df.loc[0, "keywords"])

filename = roll + "_faq_data.csv"
df.to_csv(filename, index=False)
print("Saved to", filename)


# q5
print("\nQ5: entries per category")
print(df.groupby("category")["question"].count())


# q6
def answer_query(query, df):
    result_df = score_query(query, df)

    print("\nQuery:", query)
    if len(result_df) == 0:
        print("No matching entry found.")
        return

    top_score = result_df["score"].max()
    top = result_df[result_df["score"] == top_score]

    if len(top) > 1:
        print("TIE -", len(top), "entries have the same highest score:")
    else:
        print("Best match:")

    for i in top.index:
        print("  Q:", top.loc[i, "question"])
        print("  A:", top.loc[i, "answer"])


print("\nQ6: tie-aware matching")
answer_query("fee", df)
answer_query("reset password", df)