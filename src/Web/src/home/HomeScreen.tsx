import React, { FC, useState } from 'react';
import "./HomeScreen.css"
import { RiMovie2Fill } from "react-icons/ri";
import { IconContext } from 'react-icons';
import { Slider } from '@mui/material';
import { IoMdRefresh } from "react-icons/io";
import MovieList from '../movieList/MovieList';
import { IMovie } from '../interfaces/IMovie';
import axios from 'axios';
import { ClipLoader } from 'react-spinners';

const marks1 = [
    {
        value: 0,
        label: 'Low',
    },
    {
        value: 1,
        label: 'Medium',
    },
    {
        value: 2,
        label: 'High',
    },
];

const marks2 = [
    {
        value: 0,
        label: 'Sad',
    },
    {
        value: 1,
        label: 'Neutral',
    },
    {
        value: 2,
        label: 'Funny',
    },
];
const marks3 = [
    {
        value: 0,
        label: 'Short',
    },
    {
        value: 1,
        label: 'Medium',
    },
    {
        value: 2,
        label: 'Long',
    },
];
const marks4 = [
    {
        value: 0,
        label: 'Old',
    },
    {
        value: 1,
        label: 'Between',
    },
    {
        value: 2,
        label: 'New',
    },
];

const HomeScreen: FC = (): JSX.Element => {

    const [year, setYear] = useState<number | number[]>(0)
    const [budget, setBudget] = useState<number | number[]>(0)
    const [mood, setMood] = useState<number | number[]>(0)
    const [duration, setDuration] = useState<number | number[]>(0)
    const [vote, setVote] = useState<number | number[]>(0)
    const [popularity, setPopularity] = useState<number | number[]>(0)


    const [loading, setLoading] = useState<boolean>(false)
    const [movieList, setMovieList] = useState<IMovie[]>([])

    const handleRefresh = () => {
        setLoading(true)
        axios({
            params: {
                year: year,
                budget: budget,
                mood: mood,
                duration: duration,
                vote: vote,
                popularity: popularity
            },
            method: 'get',
            headers: {
                "Access-Control-Allow-Origin": "*"
            },

            url: 'http://localhost:5000/movies',
        })
            .then((resp) => {
                setLoading(false)
                setMovieList(resp.data)
                console.log(resp)
            })
            .catch((err) => {
                setLoading(false)
                console.error(err)
            });
    }

    const MovieInit = () => {
        return (
            <div className='home-init-container'>
                <div className='home-init-button' onClick={handleRefresh}>
                    Search Movies!
                </div>
            </div>
        )
    }
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
                <div className='home-bar-refresh' onClick={handleRefresh}>
                    <IconContext.Provider
                        value={{ color: '#2C3E50', size: '26px' }}>
                        <IoMdRefresh />
                    </IconContext.Provider>
                </div>
            </div>
            <div className='home-sliders-container'>
                <div className='home-sliders-user'>
                    <div className='home-sliders'>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#FFC312' }}>
                            Year of production
                            <div className='home-sliders-one'>
                                <Slider sx={{
                                    width: 250,
                                    color: '#2C3E50',
                                }} aria-label="Year" track={false} marks={marks4} min={0} max={2} value={year} onChange={(event, v) => { setYear(v) }} />
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#D980FA' }}>
                            Budget
                            <div className='home-sliders-one'>
                                <Slider sx={{
                                    width: 250,
                                    color: '#2C3E50',
                                }} aria-label="Year" track={false} marks={marks1} min={0} max={2} value={budget} onChange={(event, v) => { setBudget(v) }} />
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#B53471' }}>
                            Mood
                            <div className='home-sliders-one'>
                                <Slider sx={{
                                    width: 250,
                                    color: '#2C3E50',
                                }} aria-label="Year" track={false} marks={marks2} min={0} max={2} value={mood} onChange={(event, v) => { setMood(v) }} />
                            </div>
                        </div>
                    </div>
                    <div className='home-sliders'>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#F79F1F' }}>
                            Duration
                            <div className='home-sliders-one'>
                                <Slider sx={{
                                    width: 250,
                                    color: '#2C3E50',
                                }} aria-label="Year" track={false} marks={marks3} min={0} max={2} value={duration} onChange={(event, v) => { setDuration(v) }} />
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#12CBC4' }}>
                            Vote score
                            <div className='home-sliders-one'>
                                <Slider sx={{
                                    width: 250,
                                    color: '#2C3E50',
                                }} aria-label="Year" track={false} marks={marks1} min={0} max={2} value={vote} onChange={(event, v) => { setVote(v) }} />
                            </div>
                        </div>
                        <div className='home-sliders-bottom' style={{ backgroundColor: '#A3CB38' }} >
                            Popularity
                            <div className='home-sliders-one'>
                                <Slider sx={{
                                    width: 250,
                                    color: '#2C3E50',
                                }} aria-label="Year" track={false} marks={marks1} min={0} max={2} value={popularity} onChange={(event, v) => { setPopularity(v) }} />
                            </div>
                        </div>
                    </div>
                </div>
                {/* <div className='home-sliders-info'>
                    <div> Year of production : {year}</div>
                    <div> Budget : {budget}</div>
                    <div> Mood : {mood}</div>
                    <div> Duration : {duration}</div>
                    <div> Vote score : {vote}</div>
                    <div> Popularity : {popularity}</div>
                </div> */}
            </div>
            {
                loading ?
                    <div className='home-init-container'>
                        <ClipLoader color={"#ED4C67"} loading={loading} size={150} />
                    </div>
                    : <>
                        {
                            movieList.length ? <MovieList movieList={movieList} /> : <MovieInit />
                        }

                    </>
            }

        </div>
    );
}

export default HomeScreen;