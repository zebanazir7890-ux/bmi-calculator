from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = ""
    color = "black"
    error = None

    if request.method == 'POST':
        try:
            # Form se data lena
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height'))

            if height <= 0:
                error = "Height 0 se zyada honi chahiye!"
            else:
                # BMI Formula: weight / (height * height)
                bmi = round(weight / (height ** 2), 2)

                # Categories decide karna
                if bmi < 18.5:
                    category = "Underweight (Kam wazan)"
                    color = "#3498db" # Blue
                elif 18.5 <= bmi < 25:
                    category = "Normal Weight (Theek wazan)"
                    color = "#2ecc71" # Green
                elif 25 <= bmi < 30:
                    category = "Overweight (Zyada wazan)"
                    color = "#f1c40f" # Yellow
                else:
                    category = "Obese (Bohot zyada wazan)"
                    color = "#e74c3c" # Red
        
        except (ValueError, TypeError):
            error = "Sahi numbers enter karein!"

    # Result ko wapas HTML page par bhejna
    return render_template('index.html', bmi=bmi, category=category, color=color, error=error)

if __name__ == '__main__':
    app.run(debug=True)