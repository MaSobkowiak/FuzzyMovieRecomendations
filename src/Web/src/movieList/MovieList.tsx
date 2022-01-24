import { useState } from 'react';
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

                <div className='movie-list-info-upper'>
                    {
                        activeMovie?.poster ? <img alt='No poster avalible' className='movie-list-info-img' src={`${activeMovie?.poster}`} /> :
                            <div className='movie-list-info-img'>
                                <IconContext.Provider
                                    value={{ color: '#2c3e5027', size: '200px' }}
                                >
                                    <BsQuestion />
                                </IconContext.Provider>
                            </div>
                    }
                    <div className='movie-list-info-upper-text'>
                        <div className='movie-list-info-upper-title'>
                            {activeMovie?.title}
                        </div>
                        <div className='movie-list-info-upper-scores'>
                            <div>
                                Accuracy: {activeMovie?.accuracy}%
                            </div>
                            <div>
                                IMDB score: {activeMovie?.score}
                            </div>
                        </div>
                        {activeMovie?.description}
                    </div>
                </div>
                <div className='movie-list-info-lower'>
                    <div className='movie-list-info-lower-column'>
                        <div className='movie-list-info-lower-element' style={{ backgroundColor: '#FFC312' }}>
                            <div style={{ fontWeight: '600' }}>
                                Year of production:
                            </div>
                            <div>
                                {activeMovie?.year}
                            </div>
                        </div>
                        <div className='movie-list-info-lower-element' style={{ backgroundColor: '#D980FA' }}>
                            <div style={{ fontWeight: '600' }}>
                                Budget
                            </div>
                            <div>
                                {activeMovie?.budget}
                            </div>
                        </div>
                        <div className='movie-list-info-lower-element' style={{ backgroundColor: '#B53471' }}>
                            <div style={{ fontWeight: '600' }}>
                                Mood
                            </div>
                            <div>
                                {activeMovie?.genre}
                            </div>
                        </div>
                    </div>
                    <div className='movie-list-info-lower-column'>
                        <div className='movie-list-info-lower-element' style={{ backgroundColor: '#F79F1F' }}>
                            <div style={{ fontWeight: '600' }}>
                                Duration
                            </div>
                            <div>
                                {activeMovie?.duration} min.
                            </div>
                        </div>
                        <div className='movie-list-info-lower-element' style={{ backgroundColor: '#12CBC4' }}>
                            <div style={{ fontWeight: '600' }}>
                                Vote score
                            </div>
                            <div>
                                {activeMovie?.score}
                            </div>
                        </div>
                        <div className='movie-list-info-lower-element' style={{ backgroundColor: '#A3CB38' }}>
                            <div style={{ fontWeight: '600' }}>
                                Popularity
                            </div>
                            <div>
                                {activeMovie?.popularity}
                            </div>
                        </div>
                    </div>
                </div>
                {/*
                <div className='movie-list-info-txt'></div>
                <div className='movie-list-info-txt'>{activeMovie?.country}</div>
                <div className='movie-list-info-txt'>{activeMovie?.genre}</div>
                <div className='movie-list-info-txt'>{activeMovie?.score}</div>
                <div className='movie-list-info-txt'>{activeMovie?.duration}</div> */}
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