document.getElementById("analyzeBtn").addEventListener("click", analyzeResume)

async function analyzeResume(){

const fileInput = document.getElementById("resumeFile")
const jobDesc = document.getElementById("jobDesc").value
const loader = document.getElementById("loader")
const button = document.getElementById("analyzeBtn")

if(!fileInput.files.length){
alert("Please upload resume")
return
}

let formData = new FormData()

formData.append("file", fileInput.files[0])
formData.append("job_description", jobDesc)

try{

loader.style.display="block"
button.disabled=true

const response = await fetch("http://127.0.0.1:8000/upload-resume",{
method:"POST",
body:formData
})

const result = await response.json()

console.log(result)

document.getElementById("atsScore").innerText = result.ATS_score + "%"

showSkills(result.skills_detected)
showMissingSkills(result.missing_skills)
showQuestions(result.interview_questions)

}catch(error){

console.error(error)
alert("Error connecting to API")

}finally{

loader.style.display="none"
button.disabled=false

}

}



function showSkills(skills){

let html=""

skills.forEach(skill=>{
html += `<span class="badge">${skill}</span>`
})

document.getElementById("skills").innerHTML = html

}



function showMissingSkills(skills){

let html=""

skills.forEach(skill=>{
html += `<span class="badge missing">${skill}</span>`
})

document.getElementById("missingSkills").innerHTML = html

}



function showQuestions(questions){

let html=""

questions.forEach(q=>{
html += `<li>${q}</li>`
})

document.getElementById("questions").innerHTML = html

}