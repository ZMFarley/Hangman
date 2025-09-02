import "./App.css";
function WelcomePage(){
 return <div className="center">
  <h1 className="title">Hangman</h1>
  <HangmanArt/>
  <button className="startingButton">Press to Start</button>
</div>;
}

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
export default WelcomePage;
