/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

export const environment = {
  production: false,
  apiServerUrl: 'https://coffeeshop-app-backend.herokuapp.com', // the running FLASK api server url
  auth0: {
    url: 'auth0-fsnd.us', // the auth0 domain prefix
    audience: 'coffeeshop', // the audience set for the auth0 app
    clientId: 'uym5IVr4gHOR3LmzTfdKYaQ5ipynyiyI', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:8100', // the base url of the running ionic application. 
  }
};
