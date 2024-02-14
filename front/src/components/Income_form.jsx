import React from 'react'
import axios from 'axios';
import { useState,useEffect } from 'react';

const Income_form = () => {
  const [type,setType] = useState('');
	const [sum,setSum] = useState('');
  const [name,setName] = useState('');
  // Create the submit method.
	const submit = async e =>{
	  e.preventDefault()
  
	  const user = {
		sum:sum,
    name:name,
		type:type,
		category:"Income",
	  };
  // Create the POST requuest
	const config = {
		headers: {
		'Content-Type': 'application/json'
		},
		withCredentials: true
	};
	const { data } = await axios.post('http://127.0.0.1:8000/api/v1/', user, config);


	
	  
	window.location.href = '/'
	}
  
	return (    
		<>
		<div className="container">
		  <form action="" className='auth_form' onSubmit={submit}>
			<div className="auth-title">Add Income</div>

      <input name='name' 
			  type="text"     
			  className="auth_input"
			  placeholder="Enter name"
			  value={name}
			  required                
			  onChange={e => setName(e.target.value)}/>

			<select className="auth_select" 
			  placeholder="выберите тип заработка" 
			   value={type}
			  required 
			  onChange={e => setType(e.target.value)}
			  >

			<option value="salary">зарплата</option>
			<option value="investment">инвестиции</option>
			<option value="passive_income">пассивный доход</option>
			<option value="hustle">hustle</option>
			
			</select>
			
			  
     
  
			<input name='sum' 
			  type="number"     
			  className="auth_input"
			  placeholder="Enter sum"
			  value={sum}
			  required                
			  onChange={e => setSum(e.target.value)}/>
  
		  <button type="submit" className="auth_btn">Submit</button>
		 
		
  
		  </form>
		</div>
		</>
	)
}

export default Income_form