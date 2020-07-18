import { combineReducers } from 'redux';
import { reducer as toastrReducer } from 'react-redux-toastr'

export const Reducers = combineReducers({
    toastr: toastrReducer
});