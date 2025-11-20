import nobelService from './nobelService';

class ApiService {
  public readonly nobel = nobelService;
}

const apiService = new ApiService();

export default apiService;
