$(document).ready(function(){
        // var country_list = [{"name":"Afghanistan"},{"name":"Brazil"},{"name":"Belgium"},{"name":"Costa Rica"},{"name":"France"},{"name":"Zimbabwe"}];
        // $("#personal_Details").mirandajs(country_list);
	$("#personal_Details_name").mirandajs(myData,{jsonNode:['person_details']});
	$("#personal_Details").mirandajs(myData,{jsonNode:['person_details']});
	$("#language_cv").mirandajs(myData);
	$("#education").mirandajs(myData,{jsonNode:['education']});
	$("#experience").mirandajs(myData, {jsonNode:['experience']});
	var myAwards = myData.awards;
          //console.log(myObject);
          for (i in myAwards) {
              $("#awards").append("<li>"+myAwards[i]);
          }
    var myOthers = myData.other;
          //console.log(myObject);
          for (i in myOthers) {
              $("#others").append("<li>"+myOthers[i]);
          }
    var myObjective = myData.objective;
          //console.log(myObject);
          for (i in myObjective) {
              $("#objective").append("<li>"+myObjective[i]);
          }
    $("p,#personal_Details_name").attr('contenteditable','true');
});