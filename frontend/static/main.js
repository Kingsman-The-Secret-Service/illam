class App extends React.Component {

    render() {
        return (
            <div>
                <Grid container spacing={24}>
                    <Grid item xs={12} >
                        <Header />
                    </Grid>
                    <Grid item xs={2}>
                        <Sidebar />
                    </Grid>
                    <Grid item xs={9} >
                        <MainContent />
                    </Grid>
                </Grid>
            </div>
        );
    }
}

class Header extends React.Component {

    render() {
        return (
            <AppBar position="static">
                <Toolbar>
                    <Typography variant="title" color="inherit" >
                        Kanaku Puthagam
                    </Typography>
                </Toolbar>
            </AppBar>
        );
    }
}

class Sidebar extends React.Component {

    render() {

        return (
            <List component="nav">
                <ListItem button component="a" href="/">
                    <ListItemIcon>
                        <Icon>dashboard</Icon>
                    </ListItemIcon>
                    <ListItemText primary="Dashboard" />
                </ListItem>
                <ListItem button>
                    <ListItemIcon>
                        <Icon>ballot</Icon>
                    </ListItemIcon>
                    <ListItemText primary="Budget" />
                </ListItem>
                <ListItem button>
                    <ListItemIcon>
                        <Icon>money</Icon>
                    </ListItemIcon>
                    <ListItemText primary="Income" />
                </ListItem>
                <ListItem button>
                    <ListItemIcon>
                        <Icon>store</Icon>
                    </ListItemIcon>
                    <ListItemText primary="Expense" />
                </ListItem>
                <ListItem button component="a" href="category">
                    <ListItemIcon>
                        <Icon>category</Icon>
                    </ListItemIcon>
                    <ListItemText primary="Category" />
                </ListItem>
                <ListItem button component="a" href="member">
                    <ListItemIcon>
                        <Icon>group</Icon>
                    </ListItemIcon>
                    <ListItemText primary="Member" />
                </ListItem>
                <ListItem button component="a" href="source">
                    <ListItemIcon>
                        <Icon>thumb_up_alt</Icon>
                    </ListItemIcon>
                    <ListItemText primary="Source" />
                </ListItem>
            </List>
        );
    }
}

class ContentTitle extends React.Component{

    render(){
        return(
            <Toolbar>
                <Typography variant="title" color="inherit" style={{flexGrow: 1}} >
                    { this.props.title }
                </Typography>
                <Tooltip title="Add Member">
                    <Button variant="fab" color="primary" aria-label="Add">
                        <Icon>add</Icon>
                    </Button>
                </Tooltip>
            </Toolbar>
        );
    }
}


ReactDOM.render(<App />, document.querySelector('#app'));