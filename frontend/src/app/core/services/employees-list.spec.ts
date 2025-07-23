import { TestBed } from '@angular/core/testing';

import { EmployeesList } from './employees-list';

describe('EmployeesList', () => {
  let service: EmployeesList;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EmployeesList);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
