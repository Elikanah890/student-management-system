document.getElementById("studentForm").addEventListener("submit", function (e) {
    e.preventDefault();
  
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const course = document.getElementById("course").value;
  
    fetch("http://127.0.0.1:8000/students", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email, course }),
    })
      .then((res) => res.json())
      .then((data) => {
        alert("Student added!");
        console.log(data);
      })
      .catch((err) => console.error("Error:", err));
  });
  