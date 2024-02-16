import React from 'react'

const Budgets_list = (props) => {
  const budgets = props.list
  return (
	<>
	<div className="incomes-list budget_per">
		{budgets.map(budget =>
			<div className="income budget_per">
				<div className="income_title">
				{budget.name}
				</div>
				<div className="income_sum">
				{budget.percentage}
				</div>
			</div>
		)}
	</div>
	</>
  )
}

export default Budgets_list