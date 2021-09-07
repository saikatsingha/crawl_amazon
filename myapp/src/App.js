import logo from './logo.svg';
import './App.css';

import {Home} from './Home';
import {Mobile} from './Mobile';
import { Navigation } from './Navigation';


import {BrowserRouter, Route, Switch} from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
    <div className="container">
      <h3 className="m-3 d-flex justify-content-center">
        saikat Singhaaaaaaaaa
      </h3>

      <Navigation/>

      <Switch>
        <Route path='/' component={Home} exact/>
        <Route path='/mobiles' component={Mobile}/>
      </Switch>

    </div>
    </BrowserRouter>
  );
}

export default App;
