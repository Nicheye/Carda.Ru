import React, { useState, useEffect } from 'react';
import axios from 'axios';
import filter from '../assets/filter_icon.png';

const AllSearch = () => {
    const [operations, setOperations] = useState([]);
    const [s_f, setS_f] = useState('');
    const [order, setOrder] = useState('');

    useEffect(() => {
        if (localStorage.getItem('access_token') === null) {
            window.location.href = '/login';
        } else {
            const fetchData = async () => {
                try {
                    const { data } = await axios.get(
                        `http://127.0.0.1:8000/api/v1/search?search=${s_f}&ordering=${order}`,
                        {
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            withCredentials: true
                        }
                    );
                    setOperations(data);
                } catch (error) {
                    console.log('not auth');
                }
            };

            fetchData();
        }
    }, [s_f, order]); // Include s_f and order in the dependency array

    return (
        <div className="all_search-wrapper">
            <div className="all_search-top">
                <div className="title all">ИСТОРИЯ ОПЕРАЦИЙ</div>
                <form action="">
                    <input
                        name="search"
                        type="text"
                        className="search_input"
                        placeholder="Enter"
                        value={s_f}
                        required
                        onChange={e => setS_f(e.target.value)}
                    />
                </form>

                <div className="filter" data-bs-toggle="dropdown" aria-expanded="false">
                    filter <img src={filter} className="filter_icon" alt="" />
                </div>

                <ul className="dropdown-menu">
                    <li>
                        <a className="dropdown-item" onClick={() => setOrder('sum')}>
                            sum up
                        </a>
                    </li>
                    <li>
                        <a className="dropdown-item" onClick={() => setOrder('-sum')}>
                            sum down
                        </a>
                    </li>
                    <li>
                        <a className="dropdown-item" onClick={() => setOrder('-created_at')}>
                            newest
                        </a>
                    </li>
					<li>
                        <a className="dropdown-item" onClick={() => setOrder('created_at')}>
                            oldest
                        </a>
                    </li>
                    
                </ul>
            </div>

            <div className="all_body">
                {operations.map(operation => (
                    <div className="operation-row" key={operation.id}>
                        <div className="operation-cat">{operation.category_r}</div>
                        <div className="operation-type">{operation.type_r}</div>
                        <div className="operation-sum">{operation.sum}</div>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default AllSearch;
