def parse_questions(text):

    categories = {
        "Technical": [],
        "Project": [],
        "HR": []
    }

    current = "Technical"

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue

        upper = line.upper()

        if "TECHNICAL" in upper:
            current = "Technical"
            continue

        elif "PROJECT" in upper:
            current = "Project"
            continue

        elif (
            "HR" in upper
            or "BEHAVIORAL" in upper
            or "HUMAN RESOURCES" in upper
        ):
            current = "HR"
            continue

        if line[0].isdigit():

            question = line.split(".", 1)[-1].strip()

            categories[current].append(
                question
            )

    return categories