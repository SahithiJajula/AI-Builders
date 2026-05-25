function RepoInput({

repo,
setRepo,
analyzeRepo

}){

return(

<div className="repoBox">

<input

type="text"

placeholder=

"owner/repository"

value={repo}

onChange={(e)=>

setRepo(

e.target.value

)

}

/>

<button

onClick={analyzeRepo}

>

Analyze Repository

</button>

</div>

)

}

export default RepoInput
