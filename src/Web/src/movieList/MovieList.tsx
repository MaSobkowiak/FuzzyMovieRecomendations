import { duration } from '@mui/material';
import React, { FC, useState } from 'react';
import { IMovie } from '../interfaces/IMovie';
import { MovieExample } from './MovieExample';
import { IoCloseCircleSharp } from "react-icons/io5";
import "./MovieList.css"
import { IconContext } from 'react-icons';


const MovieList: FC = (): JSX.Element => {

    const [activeMovie, setActiveMovie] = useState<IMovie>()

    const MovieInfo = () => {
        return (
            <div className='movie-list-info'>
                <IconContext.Provider
                    value={{ color: '#2C3E50', size: '26px' }}>
                    <IoCloseCircleSharp onClick={() => setActiveMovie(undefined)} />
                </IconContext.Provider>

                <img className='movie-list-info-img' src={`${activeMovie?.poster}`} />
                <div className='movie-list-info-txt'>{activeMovie?.title}</div>
                <div className='movie-list-info-txt'>{activeMovie?.country}</div>
                <div className='movie-list-info-txt'>{activeMovie?.genre}</div>
                <div className='movie-list-info-txt'>{activeMovie?.score}</div>
                <div className='movie-list-info-txt'>{activeMovie?.duration}</div>
            </div>
        )
    }

    const MovieCard = (props: IMovie) => {
        return (
            <div className='movie-card' onClick={() => setActiveMovie(props)}>
                <div className='movie-card-accuracy'>
                    {props.accuracy}%
                </div>
                <img className='movie-card-poster' src={`${props.poster}`} />
                <div className='movie-card-title'>
                    {props.title}
                </div>
            </div >
        )
    }

    return (
        <div className="movie-list">
            <div className='movie-list-main'>
                {MovieExample.map((movie, i) => <MovieCard {...movie} />
                )}
            </div>
            {
                activeMovie ? <MovieInfo /> : null
            }
        </div>
    );
}

export default MovieList;