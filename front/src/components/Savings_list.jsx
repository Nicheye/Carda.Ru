import React from 'react'

const Savings_list = (props) => {
  const incomes = props.list;
  console.log(incomes)
  return (
	<>
	<div className="incomes-list">
		{incomes.map(income =>
			<div className="income saving">
				<div className="income_title">
				{income.name}
				</div>
				<div className="income_sum">
				{income.sum}
				</div>
			</div>
		)}
	</div>
	</>
  )
}

export default Savings_list