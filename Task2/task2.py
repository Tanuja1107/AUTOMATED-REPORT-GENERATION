from fpdf import FPDF

# Function to analyze data from a file
def analyze_data(file_path):
    """
    Reads data from the file and performs basic analysis.
    Returns a summary dictionary.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Example data analysis
    num_lines = len(lines)
    words = [word for line in lines for word in line.split()]
    num_words = len(words)
    unique_words = set(words)
    num_unique_words = len(unique_words)

    return {
        "Total Lines": num_lines,
        "Total Words": num_words,
        "Unique Words": num_unique_words
    }

# Function to generate a PDF report
def generate_pdf_report(summary, output_path):
    """
    Generates a PDF report using FPDF library.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add title
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(0, 10, "Automated Report", ln=True, align="C")
    pdf.ln(10)

    # Add summary data
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Summary of the Analysis:", ln=True)
    pdf.ln(5)
    for key, value in summary.items():
        pdf.cell(0, 10, f"{key}: {value}", ln=True)

    # Save the PDF
    pdf.output(output_path)
    print(f"Report successfully saved as '{output_path}'")

# Main function
if __name__ == "__main__":
    # Input and output file paths
    input_file = "data.txt"  # Input file containing data
    output_file = "report.pdf"  # Output PDF file

    # Step 1: Analyze the data
    summary_data = analyze_data(input_file)

    # Step 2: Generate the PDF report
    generate_pdf_report(summary_data, output_file)
