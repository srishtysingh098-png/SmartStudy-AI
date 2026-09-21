def calculate_efficiency(study_hours, sleep_hours, subjects, score, break_minutes):

    # Study score
    study_score = min(study_hours / 8 * 40, 40)

    # Sleep score
    sleep_score = min(sleep_hours / 8 * 25, 25)

    # Test performance
    test_score = score / 100 * 25

    # Break management
    if 30 <= break_minutes <= 90:
        break_score = 10
    elif break_minutes < 30:
        break_score = 5
    else:
        break_score = 3

    efficiency = study_score + sleep_score + test_score + break_score

    return min(efficiency, 100)


def give_recommendation(
    study_hours,
    sleep_hours,
    subjects,
    score,
    break_minutes
):

    recommendations = []

    if study_hours < 3:
        recommendations.append(
            "Increase your focused study time gradually."
        )

    if sleep_hours < 7:
        recommendations.append(
            "Try to maintain a consistent sleep schedule."
        )

    if score < 50:
        recommendations.append(
            "Spend more time reviewing difficult topics."
        )
    elif score < 75:
        recommendations.append(
            "Practice more questions to improve your score."
        )
    else:
        recommendations.append(
            "Keep practicing and revise regularly."
        )

    if subjects > 5:
        recommendations.append(
            "Consider dividing subjects into smaller study sessions."
        )

    if break_minutes < 20:
        recommendations.append(
            "Take short breaks to maintain concentration."
        )

    return recommendations


print("=" * 45)
print("          SMART STUDY AI")
print("     Study Pattern Analyzer")
print("=" * 45)

study_hours = float(
    input("\nDaily study hours: ")
)

sleep_hours = float(
    input("Daily sleep hours: ")
)

subjects = int(
    input("Number of subjects: ")
)

score = float(
    input("Latest test score (%): ")
)

break_minutes = int(
    input("Average daily break time (minutes): ")
)

efficiency = calculate_efficiency(
    study_hours,
    sleep_hours,
    subjects,
    score,
    break_minutes
)

recommendations = give_recommendation(
    study_hours,
    sleep_hours,
    subjects,
    score,
    break_minutes
)

print("\n" + "=" * 45)
print("              RESULT")
print("=" * 45)

print(f"Study Efficiency Score: {efficiency:.2f}/100")

if efficiency >= 80:
    print("Level: Strong study routine")
elif efficiency >= 60:
    print("Level: Good, but can improve")
elif efficiency >= 40:
    print("Level: Needs improvement")
else:
    print("Level: Needs major improvement")

print("\nRecommendations:")

for number, recommendation in enumerate(
    recommendations,
    start=1
):
    print(f"{number}. {recommendation}")

print("\nNote: This tool provides general study guidance.")
