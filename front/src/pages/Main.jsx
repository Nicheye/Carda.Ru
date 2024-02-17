import React from 'react'
import { useState,useEffect } from 'react';
import axios from 'axios';
import ProgressBar from '../components/Progressbar';
import { Link } from 'react-router-dom';
import Incomes_list from '../components/Incomes_list';
import Savings_list from '../components/Savings_list';
import Budgetchart from '../components/Budgetchart';
import Budgets_list from '../components/Budgets_list';
import Ai_advice from '../components/Ai_advice';
import AllSearch from '../components/AllSearch';
import Detail_popup from '../components/Detail_popup';
const Main = () => {
  const [total_spends,setTotal_spends] = useState('');
  const [spends,setSpends] = useState([])
  const [financial_goals,setGoals] = useState([]);
  const [incomes,setIncomes] = useState([]);
  const [savings,setSavings] = useState([]);
  const [budgets,setBudgets] = useState([]);
  const [budgets_completion,setBudgetCompletion] = useState([]);
  const [cur_cat_for_popup,setCat_forPopup] = useState([]);
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
          setSavings(data.savings)
          setBudgets(data.budgets)
          setBudgetCompletion(data.budgets_completion)
          setSpends(data.spends)

        }
        catch (e){
          console.log('not auth')
        }
      })()};
  },[]);
  
  try{
    return (
      <>
      
      <div className="container">
      <Detail_popup operations={cur_cat_for_popup}/> 
        <div  className="financial_goal"  >
          <div className="title">ВАША ЦЕЛЬ:</div>
          <div className="title">{financial_goals[0].name}</div>
          <div className="title percent">{Math.round(financial_goals[0].already_done/financial_goals[0].sum*100)}%</div>
          
          <ProgressBar value={(financial_goals[0].already_done/financial_goals[0].sum)*100} goal={financial_goals[0].sum} />
        
        </div>

        <div className="main-wrapper">
          <div className="left-column">
          <div className="spends" data-bs-toggle="modal" data-bs-target="#staticBackdrop" onClick={() => setCat_forPopup(spends)}>
            <div className="title spend">ваши траты за месяц:</div>
            <div className="spend_num">{total_spends}</div>
            <Link to='/spend_created' className="add spend"></Link>
          </div>

          <div className="savings" data-bs-toggle="modal" data-bs-target="#staticBackdrop" onClick={() => setCat_forPopup(savings)} >
            <div className="title">сбережения</div>
            <Savings_list list={savings} />
            <Link to='/saving_created' className="add saving"></Link>
          </div>

          <div className="ai_advice">
          <div className="title">СОВЕТ AI</div>
            
            <Ai_advice/>
          </div>
          </div>

          <div className="right-column">
          <div className="incomes" data-bs-toggle="modal" data-bs-target="#staticBackdrop" onClick={() => setCat_forPopup(incomes)}>
            <div className="title">ваша прибыль за месяц:</div>
            <Incomes_list list={incomes}/>
            <Link to='/income_created' className="add income"></Link>
          </div>

          <div className="budgets" data-bs-toggle="modal" data-bs-target="#staticBackdrop"  onClick={() => setCat_forPopup(budgets)}>
            <div className="title budget">
            Ваши бюджеты <br /> на месяц:
            </div>
          <Budgetchart chart_data={budgets}/>
          <div className="subtitle">выполнение бюджетов <br /> за последние 30 дней</div>
          <Budgets_list list ={budgets_completion} />
          <Link to='/income_budget' className="add budget"></Link>
          </div>
          </div>
        
        </div>

        <AllSearch/>

      </div>
      </>
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