import { 
  LaureateCodec, NobelResponseCodec, PrizeCodec, PrizesResponseCodec,
  type Laureate, type NobelResponse, type Prize, type PrizesResponse 
} from './schemas';
import { decodeOrThrow } from './validation';
import ajaxService from '@/init/ajaxService';

class NobelService {
  async getLaureates(params: {
    offset?: number;
    limit?: number;
    birthCountry?: string;
    awardYear?: string;
    nobelPrizeCategory?: string;
  }): Promise<{ laureates: Laureate[]; totalCount: number }> {
    try {
      const cleanParams: Record<string, string | number> = {};
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== '') {
          cleanParams[key] = value;
        }
      });

      const responseData = await ajaxService.get<unknown>('laureates', { 
        params: cleanParams 
      });

      const validatedResponse = decodeOrThrow(NobelResponseCodec, responseData);
      
      return {
        laureates: validatedResponse.laureates || [],
        totalCount: validatedResponse.meta?.count || 0,
      };
    } catch (error) {
      console.error('Error fetching or validating laureates:', error);
      throw error;
    }
  }

  async getLaureatesSafe(params: {
    offset?: number;
    limit?: number;
    birthCountry?: string;
    awardYear?: string;
  }): Promise<{ laureates: Laureate[]; totalCount: number } | null> {
    try {
      const cleanParams: Record<string, string | number> = {};
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== '') {
          cleanParams[key] = value;
        }
      });

      const responseData = await ajaxService.get<unknown>('laureates', { 
        params: cleanParams 
      });

      const validatedResponse = decodeOrThrow(NobelResponseCodec, responseData);
      
      return {
        laureates: validatedResponse.laureates || [],
        totalCount: validatedResponse.meta?.count || 0,
      };
    } catch (error) {
      console.warn('Data validation warning:', error);
      return null;
    }
  }

  async getPrizes(params: {
    offset?: number;
    limit?: number;
    year?: string;
    category?: string;
  }): Promise<{ prizes: Prize[]; totalCount: number }> {
    try {
      const cleanParams: Record<string, string | number> = {};
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== '') {
          cleanParams[key] = value;
        }
      });

      const responseData = await ajaxService.get<unknown>('nobelPrizes', { 
        params: cleanParams 
      });

      const validatedResponse = decodeOrThrow(PrizesResponseCodec, responseData);
      
      return {
        prizes: validatedResponse.nobelPrizes || [],
        totalCount: validatedResponse.meta?.count || 0,
      };
    } catch (error) {
      console.error('Error fetching or validating prizes:', error);
      throw error;
    }
  }

  async getPrizesSafe(params: {
    offset?: number;
    limit?: number;
    year?: string;
    category?: string;
  }): Promise<{ prizes: Prize[]; totalCount: number } | null> {
    try {
      const cleanParams: Record<string, string | number> = {};
      Object.entries(params).forEach(([key, value]) => {
        if (value !== undefined && value !== '') {
          cleanParams[key] = value;
        }
      });

      const responseData = await ajaxService.get<unknown>('nobelPrizes', { 
        params: cleanParams 
      });

      const validatedResponse = decodeOrThrow(PrizesResponseCodec, responseData);
      
      return {
        prizes: validatedResponse.nobelPrizes || [],
        totalCount: validatedResponse.meta?.count || 0,
      };
    } catch (error) {
      console.warn('Data validation warning for prizes:', error);
      return null;
    }
  }
}

export default new NobelService();
export type { Laureate, NobelResponse, Prize, PrizesResponse };
