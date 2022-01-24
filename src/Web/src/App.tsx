import React, { FC, FormEvent, useEffect, useState } from 'react';
import './App.css';
import ClipLoader from "react-spinners/ClipLoader";
import SplashScreen from './splash/SplashScreen';
import HomeScreen from './home/HomeScreen';


const App: FC = (): JSX.Element => {

  const [splash, setSplash] = useState<boolean>(true);

  useEffect(() => {
    let splashTimeout = setTimeout(() => setSplash(false), 5 * 1000);

    return () => {
      clearTimeout(splashTimeout)
    }
  }, [])

  return (
    // <>
    //   {
    //     splash ? <SplashScreen setSplash={setSplash} /> : <HomeScreen />
    //   }
    // </>
    <>
      <HomeScreen />
    </>
  );
}

export default App;