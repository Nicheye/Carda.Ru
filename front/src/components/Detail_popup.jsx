import React from 'react'

const Detail_popup = (props) => {
  const operations = props.operations
  return (
	<div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
    <div class="modal-content">
      <div class="modal-body">
		<div className="title operations">Operations</div>
        {operations.map(opetation =>
			<div className='oper_row'>
			<div className="oper-type">{opetation.type_r} </div>  <div className="oper-sum">{opetation.sum}</div>
			</div>	
			)}
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Understood</button>
      </div>
    </div>
  </div>
</div>
  )
}

export default Detail_popup