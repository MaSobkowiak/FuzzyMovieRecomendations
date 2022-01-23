import React, { FC } from 'react';
import { Dispatch, SetStateAction } from "react";

interface ISplashScreenProps {
    setSplash: (active: boolean) => void;
}

const SplashScreen = (props: ISplashScreenProps) => {

    return (
        <div className="">
            splash
            <button onClick={() => props.setSplash(false)}></button>
        </div>
    );
}

export default SplashScreen;