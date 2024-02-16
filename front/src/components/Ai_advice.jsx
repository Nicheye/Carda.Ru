import React from 'react'
import axios from 'axios';
import { useState,useEffect } from 'react';
const Ai_advice = () => {
	const [message,setMessage] = useState('');

	useEffect(() => {
	  if(localStorage.getItem('access_token') ===null){
		window.location.href = '/login'
  
	  }
	  else{
		(async () =>{
		  try{
			const {data} = await axios.get(
			  'http://127.0.0.1:8000/api/v1/ai',{
				headers:{
				  'Content-Type':'application/json'
				},
				withCredentials:true,
			  }
			);
			setMessage(data.message);
		  }
		  catch (e){
			console.log('not auth')
		  }
		})()};
	},[]);

	try{
		return (
			<div className="ai_text_wrapper">
				
			 {message.slice(0,404)} ... 
		 
		  
			</div>
		  )
	}
	catch{
		return (
			<div className="ai_text_wrapper">		
			 loading	 
			</div>
		  )
	}
	
}

export default Ai_advice