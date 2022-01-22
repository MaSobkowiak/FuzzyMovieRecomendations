import React, { FC, FormEvent, useState } from 'react';
import './App.css';
import axios from 'axios';
import ClipLoader from "react-spinners/ClipLoader";

const acceptedTypes: string[] = [
  '.pdf'
];

const App: FC = (): JSX.Element => {

  const [file, setFile] = useState<File>();
  const [vat, setVat] = useState<string>("")
  const [total, setTotal] = useState<string>("")
  const [address, setAddress] = useState<string>("")
  const [loading, setLoading] = useState<boolean>(false)
  const [seconds, setSeconds] = useState<number>(0);

  const handleFileUpload = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const formData = new FormData();
    // @ts-ignore
    formData.append('file', file);
    setLoading(true)
    const initTime = Math.floor(Date.now() / 1000)
    axios({
      method: 'post',
      headers: {
        "Content-Type": "multipart/form-data",
        "Access-Control-Allow-Origin": "*"
      },

      data: formData,
      url: ' https://s434784-textract.herokuapp.com/invoice',
    })
      .then((resp) => {
        setTotal(resp?.data.total)
        setAddress(resp?.data.address)
        setVat(resp?.data.vat_id)
        setLoading(false)
        setSeconds(Math.floor(Date.now() / 1000) - initTime)
      })
      .catch((err) => console.error(err));
  };

  return (
    <div className="app">
      <div className="image-preview-box">
        {file ? file.name
          : <span>Current pdf name</span>
        }
      </div>

      <form onSubmit={handleFileUpload} className="form">
        <button className="file-chooser-button" type="button">
          Choose File
          <input
            className="file-input"
            type="file"
            name="file"
            accept={acceptedTypes.toString()}
            onChange={(e) => {
              if (e.target.files && e.target.files.length > 0) {
                setFile(e.target.files[0])
              }
            }} />
        </button>
        <button disabled={file?.name ? false : true} className="upload-button" type="submit">
          Upload
        </button>
      </form>
      <div className='result-form'>
        {!loading ?
          <>
            <div>
              Vat ID: {vat ? vat : "Brak danych "}
            </div>
            <div>
              Total: {total ? total : "Brak danych "}
            </div>
            <div>
              Address: {address ? address : "Brak danych "}
            </div>
          </> : <ClipLoader color={"#ffffff"} loading={loading} size={150} />

        }
      </div>
      <div className="result-form-footer">
        {
          vat ? <>
            Processed in {seconds} seconds.
          </> : null
        }
      </div>
    </div>
  );
}

export default App;