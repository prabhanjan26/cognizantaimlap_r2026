import Logo from './Logo/Logo';
import Timer from './Timer/Timer';
import './App.css';
function App() {


  return (
    <section className="app">
      <Logo />
      <h1>Travel App</h1>
      <Timer className="timer" />
    </section>
  )
}

export default App
