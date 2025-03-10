import streamlit as st

# Store student records
students = []

if "students" not in st.session_state:
    st.session_state.students = []

st.title("📚 Student Grading System")

# Sidebar menu
menu = st.sidebar.selectbox("Select an option", ["Add Student Record", "View Student Records"])

if menu == "Add Student Record":
    st.subheader("Enter Student Information")

    name = st.text_input("Enter your name:")
    rollno = st.text_input("Enter your roll number:")
    
    # Marks input
    maths = st.number_input("Enter your maths marks:", min_value=0, max_value=100, step=1)
    physics = st.number_input("Enter your physics marks:", min_value=0, max_value=100, step=1)
    urdu = st.number_input("Enter your urdu marks:", min_value=0, max_value=100, step=1)
    english = st.number_input("Enter your english marks:", min_value=0, max_value=100, step=1)
    computer = st.number_input("Enter your computer marks:", min_value=0, max_value=100, step=1)

    if st.button("Save Record"):
        student = {
            "name": name,
            "rollno": rollno,
            "marks": {
                "maths": maths,
                "physics": physics,
                "urdu": urdu,
                "english": english,
                "computer": computer
            }
        }
        st.session_state.students.append(student)
        st.success(f"✅ Record of {name} added successfully!")

        # Calculate Total & Percentage
        total = maths + physics + urdu + english + computer
        percentage = (total / 500) * 100
        
        # Determine Grade
        if 80 <= percentage <= 100:
            grade = "A"
        elif 70 <= percentage < 80:
            grade = "B"
        elif 60 <= percentage < 70:
            grade = "C"
        elif 50 <= percentage < 60:
            grade = "D"
        elif 40 <= percentage < 50:
            grade = "E"
        else:
            grade = "F"

        # Show results
        st.write(f"**Total Marks:** {total} / 500")
        st.write(f"**Percentage:** {percentage:.2f}%")
        st.write(f"**Grade:** {grade}")

elif menu == "View Student Records":
    st.subheader("📜 Student List")

    if st.session_state.students:
        for i, student in enumerate(st.session_state.students, start=1):
            st.write(f"**{i}. Name:** {student['name']}, **Roll No:** {student['rollno']}")
            st.write("📌 **Marks:**")
            st.json(student["marks"])
            st.write("---")
    else:
        st.warning("⚠ No student records found!")

