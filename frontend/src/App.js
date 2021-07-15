import React, { Component } from 'react';
import './App.css';
import FormPropsTextFields from './Components/LedInputFields';
import '@fontsource/roboto';
import { Typography } from '@material-ui/core';

class App extends Component {
  render() {
    return (
      <div className="App">
        <Typography variant="h3" component="h5">
          Control My LED Panel!
        </Typography>
        <FormPropsTextFields></FormPropsTextFields>
      </div>
    );
  }
}

export default App;
