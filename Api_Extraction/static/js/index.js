$("div#myId").dropzone({ url: "/file/post" });

// Disable all the input and select element
// $(document).ready(function(){
//         $("input[class='form-control']").attr("disabled", true);
//         $("select").attr("disabled", true);
//         $("button[id='addExperience']").attr("disabled", true);
// });
// Handle EditInfo button
// $( "#editInfo" ).click(function() {
//   $("#editInfo").hide();
//   $("#saveInfo").show();
//   $("input[class='form-control']").attr("disabled", false);
//   $("select").attr("disabled", false);
//   $("button[id='addExperience']").attr("disabled", false);
// });
// Handle addExperience button
// $("#addExperience").click(function(){
//   $(this).hide();
//   $("#addtional_experience").show(1000);
// });
// Read json file
// var myData = (function () {
//     var Data = null;
//     $.ajax({
//         'async': false,
//         'global': false,
//         'url': 'Jsonfile/vi/HR - Vu-Thi-Thu.json',
//         'dataType': "json",
//         'success': function (data) {
//             Data = data;
//         }
//     });
//     return Data;
// })();
// var myData;
//   $.getJSON('person.json', function(data){
//     myData=data;
//   });
// $.get( "http://127.0.0.1:8000/extraction/api/extract-cv", { pathfile: "nguyen_van_huy.pdf" } )
//   .done(function( data ) {
//     // alert( "Data Loaded: " + data );
//     console.log(data);
//   });


// var myData = {
//   "language_cv": "en",
//   "image": [ "D:\\Documents\\GitHub\\recruitment_recommender_system\\Api_Extraction/extract_cv/temp/5_Im6.jpeg" ],
//   "person_details": {
//     "name": "LE THI MINH HOA",
//     "birth_day": "April 8, 1994",
//     "sex": "Female",
//     "address": "Hanoi, Vietnam",
//     "mail": "minhhoalt.hr@gmail.com",
//     "number": "0979.657.048",
//     "text": [ "0979.657.048 Female Le Thi Minh Hoa Recruiter Specialist minhhoalt.hr@gmail.com April 8 1994 https www.facebook.com l Hanoi Vietnam eminhhoa94" ]
//   },
//   "education": {
//     "university": "Education 2012 - 2016 VIETNAM UNIVERSITY OF COMMERCE Major Human Resources Management GPA 3.36 4.0 Degree Very Good",
//     "cpa": "3.36",
//     "major": "Ng\u00e0nh h\u1ecdc",
//     "language": [ ],
//     "awards": [ ],
//     "text": [ "Education 2012 - 2016 VIETNAM UNIVERSITY OF COMMERCE Major Human Resources Management GPA 3.36 4.0 Degree Very Good" ]
//   },
//   "skills": {
//     "programing": [ "CMake" ],
//     "database": [ ],
//     "framework": [ ],
//     "text": [ "- Organize the training sessions and workshops aims to share the knowledge of HR and soft skills from the HR experts in many companies" ]
//   },
//   "experience": [
//     {
//       "company": "C\u00f4ng ty",
//       "project": "Project",
//       "position": "V\u1ecb tr\u00ed",
//       "time": "Th\u1eddi gian",
//       "skill": {
//         "programing": [ "C"],
//       "database": [ "SQL" ],
//       "framework": [ "Mongo" ],
//       },
      
//       "text": "Work experience TOPICA EDTECH GROUP Feb 2016 - Present Recruiter Staff"
//     },
//     {
//       "company": "C\u00f4ng ty 2",
//       "project": "Project 2",
//       "position": "V\u1ecb tr\u00ed 2",
//       "time": "Th\u1eddi gian 2",
//       "skill": {
//         "programing": [ "F"],
//       "database": [ "SQL2" ],
//       "framework": [ "Mongo2" ],
//       },
//       "text": "Learder of HR and Admin dept of Edumall Thailand product worked in Bangkok Thailand"
//     }
//   ],
//   "other": { 
//         "target": "C2",
//         "hobbies":"football"
//         },

// }
  // $("#Data_language").mirandajs(myData);
  // $("#Data_image").mirandajs(myData);
  // $("#Data_personal_details").mirandajs(myData, {jsonNode:['person_details']});
  // $("#Data_education").mirandajs(myData, {jsonNode:['education']});
  // $("#Data_skills").mirandajs(myData, {jsonNode:['skills']});
  //   var count= Object.keys(myData.experience).length;
  // console.log(count);
  // var i;
  // for(i=0;i<count; i++){
  //     $("#Data_experience").mirandajs(myData, {jsonNode:['experience[i]']});
  //     $("#Data_experience_skills").mirandajs(myData, {jsonNode:['experience[i].skill']});
  // }
  

  // $("#Data_experience_skills").mirandajs(myData, {jsonNode:['experience[1].skill']});
  // $("#Data_experience_skills").mirandajs(myData, {jsonNode:['experience[0]']});

  
  // $("#Data_others").mirandajs(myData, {jsonNode:['other']});

  // $.ajax({
  //   url: 'person.json',
  //   dataType:'json',
  //   type:'get',
  //   cache: false,
  //   success: function(data){
  //     console.log('worked!')
  //   }
  // })