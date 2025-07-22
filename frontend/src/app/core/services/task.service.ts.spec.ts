import { TestBed } from '@angular/core/testing';

import { TaskServiceTs } from './task.service.ts';

describe('TaskServiceTs', () => {
  let service: TaskServiceTs;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TaskServiceTs);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
