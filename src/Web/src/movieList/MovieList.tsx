import React, { useState } from 'react';
import { IMovie } from '../interfaces/IMovie';
import { IoCloseCircleSharp } from "react-icons/io5";
import { BsQuestion } from "react-icons/bs";
import "./MovieList.css"
import { IconContext } from 'react-icons';

interface IMovieListProps {
    movieList: IMovie[]
}

const MovieList = (props: IMovieListProps): JSX.Element => {

    const [activeMovie, setActiveMovie] = useState<IMovie>()

    const MovieInfo = () => {
        return (
            <div className='movie-list-info'>
                <IconContext.Provider
                    value={{ color: '#2C3E50', size: '26px' }}>
                    <IoCloseCircleSharp onClick={() => setActiveMovie(undefined)} />
                </IconContext.Provider>

                {
                    activeMovie?.poster ? <img alt='No poster avalible' className='movie-list-info-img' src={`${activeMovie?.poster}`} /> :
                        <div className='movie-card-poster-none'>
                            <IconContext.Provider
                                value={{ color: '#2c3e5027', size: '200px' }}
                            >
                                <BsQuestion />
                            </IconContext.Provider>
                        </div>
                }

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
                {
                    props.poster ? <img alt='No poster avalible' className='movie-card-poster' src={`${props.poster}`} /> :

                        <div className='movie-card-poster-none'>
                            <IconContext.Provider
                                value={{ color: '#2c3e5027', size: '200px' }}
                            >
                                <BsQuestion />
                            </IconContext.Provider>
                        </div>
                }

                <div className='movie-card-title'>
                    {props.title}
                </div>
            </div >
        )
    }

    return (
        <div className="movie-list">
            <div className='movie-list-main'>
                {props.movieList.map((movie, i) => <MovieCard {...movie} />
                )}
            </div>
            {
                activeMovie ? <MovieInfo /> : null
            }
        </div>
    );
}

export default MovieList;