import "./App.css";
import { useState } from "react";

//Interface to handle transition props
interface PageTransitions {
  startGame?: () => void
  playGame?: () => void
  endGame?: () => void
  chooseReplay?: () => void
}

//Entry page to game
function WelcomePage({startGame}: PageTransitions){
 return <div className="center">
  <h1 className="title">Hangman</h1>
  <HangmanArt/>
  <button className="startingButton"onClick={startGame}>Press to Start</button>
</div>;
}

//Rules for the user, which will be reiterated upon when errors occur
function RulePage({playGame}: PageTransitions){
  return <div className="center">
    <h1 className="subtitle">Rules:</h1>
    <ol className="rules">
      <li>Only one letter can be guessed at a time</li>
      <li>You have 6 wrong guesses before you lose</li>
      <li>Hyphens and commas are potentially in the word</li>
      <li>Have fun!</li>
    </ol>
    <button className="startingButton" onClick={playGame}>Start Round</button>
  </div>
}

//Main Game page
function GamePage({endGame}: PageTransitions){
 return (
    <div className="center">
      <HangmanArt/>
      <button className="startingButton" onClick={endGame}>End Round</button>
    </div>
 );
}

//Leaderboard Page
function LeaderboardPage({chooseReplay}: PageTransitions){
 return (
    <div className="center">
      <h1 className="title">Leaderboard:</h1>
      <button className="startingButton" onClick={chooseReplay}>Restart</button>
    </div>
 );
}
//Basic Front Page Art, only used for the welcome page
function HangmanArt(){
  return (
  <pre className="welcomeGallows">
    {String.raw`
      ______	 
      |    |	
      O    |
     /|\   |	
     / \   |
    _______|
    `}
  </pre>
  );
}

//Main entry portion of the game, moving throughout the different pages 
function App(){
  //State to manage the movement throughout the pages
  const [page, setPage] = useState("WelcomePage");

  //Conditional to branch to the welcome page
  if (page === "WelcomePage"){
    return <WelcomePage startGame ={() => setPage("RulePage")}/>
  }

  //Conditional to branch to the rule page
  else if (page === "RulePage"){
      return <RulePage playGame ={() => setPage("GamePage")}/>
  }

  //Conditional to branch to the rule page
  else if (page === "GamePage"){
      return <GamePage endGame ={() => setPage("LeaderboardPage")}/>
  }

  //Conditional to branch to the rule page
  else if (page === "LeaderboardPage"){
      return <LeaderboardPage chooseReplay ={() => setPage("WelcomePage")}/>
  }
  return null;
}


export default App;
