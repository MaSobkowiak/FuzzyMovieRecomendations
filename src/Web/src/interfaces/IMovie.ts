export interface IMovie {
    id: string;
    title: string;
    poster?: string;
    country: string;
    accuracy: number;
    description: string;

    year: string;
    budget: string;
    genre: any;
    duration: number;
    score: number;
    popularity: string;
}