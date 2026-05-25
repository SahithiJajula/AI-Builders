function Findings({

title,
items

}){

return(

<div className="findingBox">

<h3>

{title}

</h3>

{

items.length===0 ?

<p>

No Issues Found

</p>

:

<ul>

{

items.map(

(item,index)=>(

<li key={index}>

{item}

</li>

)

)

}

</ul>

}

</div>

)

}

export default Findings
