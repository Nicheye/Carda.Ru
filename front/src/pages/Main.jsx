import React from 'react'
import { useState,useEffect } from 'react';
import axios from 'axios';
import ProgressBar from '../components/Progressbar';
import { Link } from 'react-router-dom';
import Incomes_list from '../components/Incomes_list';

const Main = () => {
  const [total_spends,setTotal_spends] = useState('');
  const [financial_goals,setGoals] = useState([]);
  const [incomes,setIncomes] = useState([]);

  useEffect(() => {
    if(localStorage.getItem('access_token') ===null){
      window.location.href = '/login'

    }
    else{
      (async () =>{
        try{
          const {data} = await axios.get(
            'http://127.0.0.1:8000/api/v1/',{
              headers:{
                'Content-Type':'application/json'
              },
              withCredentials:true,
            }
          );
          console.log(data.incomes_total);
          setTotal_spends(data.incomes_total);
          setGoals(data.goals)
          setIncomes(data.incomes)

        }
        catch (e){
          console.log('not auth')
        }
      })()};
  },[]);
  
  try{
    return (
      <div className="container">
        <div className="financial_goal">
          <div className="title">ВАША ЦЕЛЬ:</div>
          <div className="title">{financial_goals[0].name}</div>
          <div className="title percent">{Math.round(financial_goals[0].already_done/financial_goals[0].sum*100)}%</div>
          
          <ProgressBar value={(financial_goals[0].already_done/financial_goals[0].sum)*100} goal={financial_goals[0].sum} />
        
        </div>

        <div className="main-wrapper">
          <div className="spends">
            <div className="title spend">ваши траты за месяц:</div>
            <div className="spend_num">{total_spends}</div>
            <Link to='/spend_created' className="add spend"></Link>
          </div>

          <div className="incomes">
            <div className="title">ваша прибыль за месяц:</div>
            <Incomes_list list={incomes}/>
            <Link to='/income_created' className="add income"></Link>
          </div>
        </div>


      </div>
      )
  }
  catch{
    return(
      <>
      laoding
      </>
    )
  }
    
  
  
  
}

export default Main