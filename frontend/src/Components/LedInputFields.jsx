import React from 'react';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import Snackbar from '@material-ui/core/Snackbar';
import Button from '@material-ui/core/Button';
import MuiAlert from '@material-ui/lab/Alert';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    root: {
        '& .MuiTextField-root': {
            margin: theme.spacing(1),
            width: '25ch',
        },
    },
}));

function Alert(props) {
    return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const operations = [
    {
        value: 'Picture',
        label: 'Picture',
    },
    {
        value: 'Text',
        label: 'Text',
    },
    {
        value: 'ScrollingText',
        label: 'Scrolling Text',
    },
];

export default function FormPropsTextFields() {
    const classes = useStyles();

    const [operation, setOperation] = React.useState('ScrollingText');

    const handleChange = (event) => {
        setOperation(event.target.value);
    };

    const [open, setOpen] = React.useState(false);

    const handleClick = () => {
        setOpen(true);
    };

    const handleClose = (event, reason) => {
        if (reason === 'clickaway') {
            return;
        }

        setOpen(false);
    };

    return (
        <div className="inputContainer">
            <form className={classes.root} autoComplete="off">
                <div>
                    <TextField
                        id="select-operation"
                        select
                        label="Select an Operation"
                        value={operation}
                        onChange={handleChange}
                        helperText="What are you sending to the panel?"
                    >
                        {operations.map((option) => (
                            <MenuItem key={option.value} value={option.value}>
                                {option.label}
                            </MenuItem>
                        ))}
                    </TextField>
                    <TextField required id="user-parameter" label="Image URL/Text to display" defaultValue="Hello World!" />
                    <TextField required type="password" id="password" label="API Key" helperText="Ask me for this :)" />
                </div>
            </form>
            <Button color="primary" variant="contained" onClick={handleClick}>
                Submit
            </Button>
            <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
                <Alert onClose={handleClose} severity="success">
                    You have successfully updated the panel!
                </Alert>
            </Snackbar>
        </div>
    );
}