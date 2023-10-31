export const oneUpdate = async (query,update,model) => {
    try{
        return await model.findOneAndUpdate(query,update)
    }catch(err){
        console.log(err)
    }
}
export const one = async (query,model) => {
    try{
        return await model.findOne(query)
    }catch(err){
        console.log(err)
    }
}
export const multiple = async (query,model) => {
    try{
        return await model.find(query)
    }catch(err){
        console.log(err)
    }
}