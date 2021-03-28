function validation_1()
{
    var have_account = document.getElementById("have_account").value;
    var No_account = document.getElementById("No_account").value;

    if (have_account==0 && No_account==0)
    {
        alert("Fill the ");
        return false;

    }


}