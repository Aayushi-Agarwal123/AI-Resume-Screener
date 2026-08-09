import "./CandidateSearch.css";

type Props = {
  search:string;
  setSearch:(v:string)=>void;
}

function CandidateSearch({
search,
setSearch
}:Props){

return(

<input

className="candidate-search"

placeholder="Search Candidate..."

value={search}

onChange={(e)=>

setSearch(e.target.value)

}

/>

)

}

export default CandidateSearch;