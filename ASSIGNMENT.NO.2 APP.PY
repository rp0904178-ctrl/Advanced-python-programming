# Dynamic Report Generator
# Experiment No. 2

# Decorator for converting report text to uppercase
def uppercase(func):
    def wrapper(self):
        return func(self).upper()
    return wrapper


# Decorator for adding a border to the report
def add_border(func):
    def wrapper(self):
        text = func(self)
        border = "*" * 50
        return f"{border}\n{text}\n{border}"
    return wrapper


# Decorator for formatting the title
def format_title(func):
    def wrapper(self):
        text = func(self)
        lines = text.split("\n")

        if lines:
            lines[0] = lines[0].center(50, "-")

        return "\n".join(lines)

    return wrapper


class Report:
    # Constructor - Magic Method
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method for creating a report from a template
    @classmethod
    def from_template(cls, template, data):
        title = template.format(**data)
        content = (
            f"Name: {data.get('name', 'N/A')}\n"
            f"Department: {data.get('department', 'N/A')}\n"
            f"Score: {data.get('score', 'N/A')}\n"
            f"Status: {data.get('status', 'N/A')}"
        )

        return cls(title, content)

    # Formatting the report
    @add_border
    @format_title
    def generate(self):
        return f"{self.title}\n{self.content}"

    # Magic Method - string representation
    def __str__(self):
        return self.generate()

    # Magic Method - returns length of report
    def __len__(self):
        return len(self.generate())


# Main Program
print("===== Dynamic Report Generator =====\n")

# Data for first report
student1 = {
    "name": "Rahul",
    "department": "Computer Engineering",
    "score": 88,
    "status": "PASS"
}

# Creating report using class method
report1 = Report.from_template(
    "STUDENT PERFORMANCE REPORT",
    student1
)

print(report1)
print("\nReport Length:", len(report1))


# Data for second report
student2 = {
    "name": "Priya",
    "department": "Information Technology",
    "score": 95,
    "status": "PASS"
}

# Creating another report
report2 = Report.from_template(
    "ACADEMIC PERFORMANCE REPORT",
    student2
)

print("\n" + str(report2))
print("\nReport Length:", len(report2))


# Demonstrating uppercase decorator separately
class UpperCaseReport(Report):

    @uppercase
    def generate_uppercase(self):
        return f"{self.title}\n{self.content}"


upper_report = UpperCaseReport(
    "MONTHLY REPORT",
    "This is a dynamically formatted report."
)

print("\n===== Uppercase Report =====")
print(upper_report.generate_uppercase())
