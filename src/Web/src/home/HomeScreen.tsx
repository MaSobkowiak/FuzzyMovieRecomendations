import React, { FC, useState } from 'react';
import "./HomeScreen.css"
import { RiMovie2Fill } from "react-icons/ri";
import { IconContext } from 'react-icons';
import { Slider } from '@mui/material';
import MovieList from '../movieList/MovieList';


const HomeScreen: FC = (): JSX.Element => {

    const [year, setYear] = useState<number | number[]>(0)
    const [budget, setBudget] = useState<number | number[]>(0)
    const [mood, setMood] = useState<number | number[]>(0)
    const [duration, setDuration] = useState<number | number[]>(0)
    const [vote, setVote] = useState<number | number[]>(0)
    const [popularity, setPopularity] = useState<number | number[]>(0)

    return (
        <div className="home-container">
            <div className='home-bar'>
                <IconContext.Provider
                    value={{ color: '#2C3E50', size: '26px' }}>
                    <RiMovie2Fill />
                </IconContext.Provider>
                <div className='home-bar-title'>
                    Movie Recomendations
                </div>
            </div>
            <div className='home-sliders-container'>
                <div className='home-sliders-user'>
                    <div className='home-sliders'>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#FFC312' }}>
                            Year of production
                            <div className='home-sliders-one'>
                                Old
                                <Slider sx={{
                                    width: 180,
                                    color: '#2C3E50',
                                }} aria-label="Year" min={10} max={100} value={year} onChange={(event, v) => { setYear(v) }} />
                                New
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#D980FA' }}>
                            Budget
                            <div className='home-sliders-one'>
                                Low
                                <Slider sx={{
                                    width: 180,
                                    color: '#2C3E50',
                                }} aria-label="Year" min={10} max={100} value={budget} onChange={(event, v) => { setBudget(v) }} />
                                High
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#B53471' }}>
                            Mood
                            <div className='home-sliders-one'>
                                Sad
                                <Slider sx={{
                                    width: 180,
                                    color: '#2C3E50',
                                }} aria-label="Year" min={10} max={100} value={mood} onChange={(event, v) => { setMood(v) }} />
                                Funny
                            </div>
                        </div>
                    </div>
                    <div className='home-sliders'>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#F79F1F' }}>
                            Duration
                            <div className='home-sliders-one'>
                                Short
                                <Slider sx={{
                                    width: 180,
                                    color: '#2C3E50',
                                }} aria-label="Year" min={10} max={100} value={duration} onChange={(event, v) => { setDuration(v) }} />
                                Long
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#12CBC4' }}>
                            Vote score
                            <div className='home-sliders-one'>
                                Low
                                <Slider sx={{
                                    width: 180,
                                    color: '#2C3E50',
                                }} aria-label="Year" min={10} max={100} value={vote} onChange={(event, v) => { setVote(v) }} />
                                High
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#A3CB38' }} >
                            Popularity
                            <div className='home-sliders-one'>
                                Low
                                <Slider sx={{
                                    width: 180,
                                    color: '#2C3E50',
                                }} aria-label="Year" min={10} max={100} value={popularity} onChange={(event, v) => { setPopularity(v) }} />
                                High
                            </div>
                        </div>
                    </div>
                </div>
                <div className='home-sliders-info'>
                    <div> Year of production : {year}</div>
                    <div> Budget : {budget}</div>
                    <div> Mood : {mood}</div>
                    <div> Duration : {duration}</div>
                    <div> Vote score : {vote}</div>
                    <div> Popularity : {popularity}</div>
                </div>
            </div>
            <MovieList />
        </div>
    );
}

export default HomeScreen;