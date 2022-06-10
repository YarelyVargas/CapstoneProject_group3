$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});

// call Flask API endpoint
function makePredictions() {
    var AgeCategory = $("#AgeCategory").val();
    var Race = $("#Race").val();
    var Diabetic = $("#Diabetic").val();
    var GenHealth = $("#GenHealth").val();
    var SkinCancer = $("#SkinCancer").val();
    var KidneyDisease = $("#KidneyDisease").val();
    var Asthma = $("#Asthma").val();
    var PhysicalActivity = $("#PhysicalActivity").val();
    var Sex = $("#Sex").val();
    var DiffWalking = $("#DiffWalking").val();
    var Stroke = $("#Stroke").val();
    var AlcoholDrinking = $("#AlcoholDrinking").val();
    var Smoking = $("#Smoking").val();
    var MentalHealth = $("#MentalHealth").val();
    var PhysicalHealth = $("#PhysicalHealth").val();
    var BMI = $("#BMI").val();


    // check if inputs are valid

    // create the payload
    var payload = {
        "AgeCategory": AgeCategory,
        "Race": Race,
        "Diabetic": Diabetic,
        "SkinCancer": SkinCancer,
        "KidneyDisease": KidneyDisease,
        "Asthma": Asthma,
        "PhysicalActivity": PhysicalActivity,
        "Sex": Sex,
        "DiffWalking": DiffWalking,
        "Stroke": Stroke,
        "AlcoholDrinking": AlcoholDrinking,
        "Smoking": Smoking,
        "MentalHealth": MentalHealth,
        "PhysicalHealth": PhysicalHealth,
        "BMI": BMI,
        "GenHealth": GenHealth }

    
    // var payload = {'BMI': '28.87',
    //  'PhysicalHealth': '6.0',
    //   'MentalHealth': '0', 
    //   'Smoking': 'Yes',
    //    'AlcoholDrinking': 'No',
    // 'Stroke': 'No',
    //  'DiffWalking': 'Yes', 
    //  'Sex': 'Female', 
    //  'PhysicalActivity': 'No',
    //   'Asthma': 'No',
    // 'KidneyDisease': 'No', 
    // 'SkinCancer':'No', 
    // "AgeCategory": '75-79',
    //  'Race': 'Black', 
    //  'Diabetic': 'No', 
    //  'GenHealth':'Fair'}

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);

            if (returnedData["prediction"] == 1) {
                $("#output").text("Please Check with your Doctor, you may have Heart Disease");
            } else {
                $("#output").text("Our results show you are HEALTHY!");
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
