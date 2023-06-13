import axiosInstance from './index'

const axios = axiosInstance

export const getid = () => { return axios.get('http://localhost:8000') }