import React,{Component} from "react";
import {Table} from 'react-bootstrap';

export class Mobile extends Component {

  constructor(props){
    super(props);
    this.state={deps:[]}
  }

  refreshList(){
    fetch(process.env.REACT_APP_API+'mobile')
    .then(response=>response.json())
    .then(data=>{
      this.setState({deps:data})
    });
  }

  componentDidMount(){
    this.refreshList();
  }

  render(){
    const {deps}=this.state;
    return(
      <div>
        <Table className="mt-4" striped bordered hover size="sm">
          <thead>
            <tr>Product_detailsId</tr>
            <tr>product_type</tr>
            <tr>company_name</tr>
          </thead>
          <tbody>
            {deps.map(dep=>
              <tr key={dep.Product_detailsId}>
              <td>{dep.product_type}</td>
              <td>{dep.company_name}</td>
            </tr>)}
          </tbody>

        </Table>  
        Mobile PAGE
      </div>
    )
  }
}