import React from 'react'
import axios from 'axios';
import { useState,useEffect } from 'react';
import Select from 'react-select'
const Spend_form = () => {
	const [type,setType] = useState('');
	const [sum,setSum] = useState('');
  // Create the submit method.
	const submit = async e =>{
	  e.preventDefault()
  
	  const user = {
		sum:sum,
		type:type,
		category:"Spend",
	  };
  // Create the POST requuest
	const config = {
		headers: {
		'Content-Type': 'application/json'
		},
		withCredentials: true
	};
	const { data } = await axios.post('http://127.0.0.1:8000/api/v1/', user, config);


	const options = [
		{ value: 'chocolate', label: 'Chocolate' },
		{ value: 'strawberry', label: 'Strawberry' },
		{ value: 'vanilla', label: 'Vanilla' }
	  ]
	  
	window.location.href = '/'
	}
  
	return (    
		<>
		<div className="container">
		  <form action="" className='auth_form' onSubmit={submit}>
			<div className="auth-title">Add Spend</div>
			
			<select className="auth_select" 
			  placeholder="выберите тип покупки" 
			   value={type}
			  required 
			  onChange={e => setType(e.target.value)}
			  >

			<option value="supermarkets">супермаркеты</option>
			<option value="games">игры</option>
			<option value="tech">техника</option>
			<option value="art">творчество</option>
			<option value="shit">всякая хуйня</option>
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

export default Spend_form