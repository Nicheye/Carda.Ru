import React,{useState} from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom';
// Define the Login function.
const Register = () => {
  const [username,setUsername] = useState('');
  const [password,setPassword] = useState('');
  const [email,setEmail] = useState('');
  const [name,setName] = useState('');
  const [second_name,setSecond_name] = useState('');
  const [date_birth,setData_birth] = useState('');
// Create the submit method.
  const submit = async e =>{
    e.preventDefault()

    const user = {
      username:username,
      password:password,
      email:email,
      name:name,
      second_name: second_name,
      date_birth: date_birth
    };
// Create the POST requuest


    await fetch('http://localhost:8000/register/',{
      method:'POST',
      headers:{'Content-Type':"application/json"},
      body: JSON.stringify(
        {
          username,
          password,
          name,
          second_name,
          date_birth
        }
      )
    });
    window.location.href='/login'
  
  }

  return (
    <div className="container">
        <form action="" className='auth_form' onSubmit={submit}>
          <div className="auth-title">Login</div>

          <input className="auth_input" 
            placeholder="Username" 
            name='username'  
            type='text' value={username}
            required 
            onChange={e => setUsername(e.target.value)}/>

          <input name='email' 
            type="email"     
            className="auth_input"
            placeholder="Enter email"
            value={email}
            required                
            onChange={e => setEmail(e.target.value)}/>

          
          <input name='name' 
            type="text"     
            className="auth_input"
            placeholder="Enter Name"
            value={name}
            required                
            onChange={e => setName(e.target.value)}/>


            <input name='second_name' 
            type="text"     
            className="auth_input"
            placeholder="Enter Second name"
            value={second_name}
            required                
            onChange={e => setSecond_name(e.target.value)}/>

          <input name='date_birth' 
            type="date"     
            className="auth_input"
            placeholder="Enter Second name"
            value={date_birth}
            required                
            onChange={e => setData_birth(e.target.value)}/>



          <input name='password' 
            type="password"     
            className="auth_input"
            placeholder="Enter password"
            value={password}
            required                
            onChange={e => setPassword(e.target.value)}/>

        <button type="submit" className="auth_btn">Submit</button>
        <Link to='/login' className="auth-link"> have acc? login</Link>
      

        </form>
      </div>
  )
}

export default Register