const analyzeBtn =
    document.getElementById("analyzeBtn");

const generateBtn =
    document.getElementById("generateBtn");

const resumeFile =
    document.getElementById("resumeFile");

const fileName =
    document.getElementById("fileName");

const analysisPopup =
    document.getElementById("analysisPopup");

const popupTitle =
    document.querySelector(".popup-card h2");

const popupText =
    document.querySelector(".popup-card p");

/* TEMPLATE SELECTION SELECTORS */
const templateModal = document.getElementById("templateModal");
const closeTemplateBtn = document.getElementById("closeTemplateBtn");
const confirmTemplateBtn = document.getElementById("confirmTemplateBtn");
const templateItems = document.querySelectorAll(".template-item");
let selectedTemplateId = null;


/* ======================================
   SHOW FILE NAME
====================================== */

resumeFile.addEventListener("change", function () {

    if (this.files.length > 0) {

        fileName.innerText =
            "Uploaded: " + this.files[0].name;

        fileName.classList.add("active");
    }

    else {

        fileName.innerText =
            "No file selected";

        fileName.classList.remove("active");
    }
});


/* ======================================
   SHOW POPUP
====================================== */

function showPopup(title, text) {

    popupTitle.innerText = title;

    popupText.innerText = text;

    analysisPopup.style.display = "flex";
}


/* ======================================
   HIDE POPUP
====================================== */

function hidePopup() {

    analysisPopup.style.display = "none";
}


/* ======================================
   ANALYZE RESUME
====================================== */

analyzeBtn.addEventListener("click", async (e) => {

    e.preventDefault();

    const jobDesc =
        document.getElementById("jobDesc").value;

    if (!resumeFile.files.length) {

        alert("Please upload resume");
        return;
    }

    const formData = new FormData();

    formData.append(
        "file",
        resumeFile.files[0]
    );

    formData.append(
        "job_description",
        jobDesc
    );

    showPopup(
        "AI Resume Analysis Running",
        "Please wait while AI analyzes your resume..."
    );

    try {

        const response = await fetch(

            "http://127.0.0.1:8000/upload-resume",

            {
                method: "POST",
                body: formData
            }
        );

        const data =
            await response.json();

        hidePopup();

        console.log(data);

        /* ATS SCORE */

        document.getElementById(
            "atsScore"
        ).innerText =
            `${data.ATS_score || 0}%`;

        /* DETECTED SKILLS */

        const skills =
            document.getElementById(
                "skills"
            );

        skills.innerHTML = "";

        (data.skills_detected || [])
        .forEach(skill => {

            skills.innerHTML += `

                <div class="skill detected">
                    ${skill}
                </div>

            `;
        });

        /* MISSING SKILLS */

        const missingSkills =
            document.getElementById(
                "missingSkills"
            );

        missingSkills.innerHTML = "";

        (data.missing_skills || [])
        .forEach(skill => {

            missingSkills.innerHTML += `

                <div class="skill missing">
                    ${skill}
                </div>

            `;
        });

        /* QUESTIONS */

        const questions =
            document.getElementById(
                "questions"
            );

        questions.innerHTML = "";

        (data.interview_questions || [])
        .forEach(question => {

            questions.innerHTML += `
                <li>${question}</li>
            `;
        });

    }

    catch(error){

        console.log(error);

        hidePopup();

        alert("Server Error");
    }
});


/* ======================================
   GENERATE RESUME (MODAL COUPLING INTERCEPTOR)
====================================== */

generateBtn.addEventListener("click", (e) => {
    e.preventDefault();

    if (!resumeFile.files.length) {
        alert("Please upload resume");
        return;
    }

    // Clear previous settings
    selectedTemplateId = null;
    templateItems.forEach(item => item.classList.remove("selected"));
    confirmTemplateBtn.disabled = true;

    // Show modal
    templateModal.style.display = "flex";
});

closeTemplateBtn.addEventListener("click", () => {
    templateModal.style.display = "none";
});

templateModal.addEventListener("click", (e) => {
    if (e.target === templateModal) {
        templateModal.style.display = "none";
    }
});

templateItems.forEach(item => {
    item.addEventListener("click", () => {
        templateItems.forEach(i => i.classList.remove("selected"));
        item.classList.add("selected");
        
        selectedTemplateId = item.getAttribute("data-template-id");
        confirmTemplateBtn.disabled = false;
    });
});

confirmTemplateBtn.addEventListener("click", async () => {
    if (!selectedTemplateId) return;

    templateModal.style.display = "none";

    const jobDesc = document.getElementById("jobDesc").value;
    const formData = new FormData();

    formData.append("file", resumeFile.files[0]);
    formData.append("job_description", jobDesc);
    formData.append("template_id", String(selectedTemplateId));

    showPopup(
        "Generating ATS Resume",
        "Please wait while AI creates ATS resume..."
    );

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/generate-resume",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();
        console.log(data);

        hidePopup();

        /* LOCALSTORAGE REGISTRATION */
        localStorage.setItem(
            "generatedResume",
            JSON.stringify(data)
        );

        // This key guarantees the next page can switch CSS styles dynamically
        localStorage.setItem("selectedTemplateId", String(selectedTemplateId));

        window.location.href = "resume.html";
    }
    catch(error){
        console.log(error);
        hidePopup();
        alert("Server Error");
    }
});