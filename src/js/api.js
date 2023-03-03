async function getData(){
   const response= await fetch('https://localhost:8080/api/json/v1/1/search.php?s=margarita%’)
   console.log(response);
   const data= await response.json();
   console.log(data);
   length=data.drinks.length;
   console.log(data);
   var temp="";
   for(i=0;i<length;i++)
   {
      temp+="<tr>";
      temp+="<td>"+data.drinks[i].strDrink+"</td>";
      temp+="<td>"+data.drinks[i].strInstructions+"</td>";
   }
    return temp;
}
